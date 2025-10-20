import json
import os

from app.core.custom_exceptions import ObjectAlreadyExistsException
from app.core.dependencies.database_dependency import db_session_dependency
from app.locations.factories.district_factory import DistrictRepositoryFactory
from app.locations.factories.facility_factory import FacilityRepositoryFactory
from app.locations.factories.region_factory import RegionRepositoryFactory
from app.locations.factories.sub_district_factory import SubDistrictRepositoryFactory
from app.locations.schemas.request.district import CreateDistrictSchema
from app.locations.schemas.request.facility import CreateFacilitySchema
from app.locations.schemas.request.region import CreateRegionSchema
from app.locations.schemas.request.sub_district import CreateSubDistrictSchema


def create_locations(*, file_path: str) -> None:
    """Create default locations data.

    Args:
        file_path (str): The path to the json file data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Locations json file not found: {file_path}")

    region_ids = {}
    district_ids = {}
    sub_district_ids = {}

    print("-------------------------CREATING LOCATIONS-------------------------")
    with open(file=file_path, mode="r") as locations_file:
        try:
            db_session = next(db_session_dependency())  # type: ignore

            region_repository = RegionRepositoryFactory.create(db_session=db_session)
            district_repository = DistrictRepositoryFactory.create(db_session=db_session)
            sub_district_repository = SubDistrictRepositoryFactory.create(db_session=db_session)
            facility_repository = FacilityRepositoryFactory.create(db_session=db_session)

            locations_dict = json.load(fp=locations_file)

            print("\n")
            print("--------------------CREATING REGIONS---------------------------")
            for number, region in enumerate(locations_dict, start=1):
                new_region_data = CreateRegionSchema(name=region)
                try:
                    new_region = region_repository.create(data=new_region_data)
                    print(f"{number}. Region {new_region.name} created.")
                    region_ids[new_region.name] = str(new_region.id)
                except ObjectAlreadyExistsException as e:
                    print(str(e), new_region_data.name)
                    region_ids[new_region_data.name] = region_repository.get_by_field(  # type: ignore
                        field_name="name", value=region, operator="eq"
                    ).id

            print("DONE")

            print("\n")
            print("--------------------CREATING DISTRICTS------------------------")
            for region, region_values in locations_dict.items():
                # region_id = region_repository.get_by_field(field_name="name", value=region)
                region_id = region_ids[region]

                if not region_id:
                    print(f"Skipping districts for unknown region: {region}")
                    continue

                for number, district in enumerate(region_values, start=1):
                    new_district_data = CreateDistrictSchema(name=district, region_id=region_id)
                    try:
                        new_district = district_repository.create(data=new_district_data)
                        print(f"{number}. District {new_district.name} created.")
                        district_ids[new_district.name] = str(new_district.id)
                    except ObjectAlreadyExistsException as e:
                        print(str(e), new_district_data.name)
                        district_ids[new_district_data.name] = district_repository.get_by_field(  # type: ignore
                            field_name="name", value=district, operator="eq"
                        ).id
            print("DONE")

            print("\n")
            print("------------------CREATING SUB DISTRICTS---------------------")
            for _, region_values in locations_dict.items():
                for district, district_values in region_values.items():
                    # district_id = district_repository.get_by_field(field_name="name", value=district)
                    district_id = district_ids[district]
                    if not district_id:
                        print(f"Skipping sub_districts for unknown district: {district}")
                        continue

                    for number, sub_district in enumerate(district_values, start=1):
                        new_sub_district_data = CreateSubDistrictSchema(name=sub_district, district_id=district_id)
                        try:
                            new_sub_district = sub_district_repository.create(data=new_sub_district_data)
                            print(f"{number}. Sub District {new_sub_district.name} created.")
                            sub_district_ids[new_sub_district.name] = str(new_sub_district.id)
                        except ObjectAlreadyExistsException as e:
                            print(str(e), new_sub_district_data.name)
                            sub_district_ids[new_sub_district_data.name] = sub_district_repository.get_by_field(  # type: ignore
                                field_name="name", value=sub_district, operator="eq"
                            ).id
            print("DONE")

            print("\n")
            print("-----------------CREATING FACILITIES------------------------")
            for _, region_values in locations_dict.items():
                for _, district_values in region_values.items():
                    for sub_district, sub_district_values in district_values.items():
                        # sub_district_id = sub_district_repository.get_by_field(field_name="name", value=sub_district)
                        print("sub district: ", sub_district)
                        sub_district_id = sub_district_ids[sub_district]
                        print(sub_district_id)
                        if not sub_district_id:
                            print(f"Skipping facilities for unknown sub_district: {sub_district}")
                            continue

                        for number, facility in enumerate(sub_district_values, start=1):
                            new_facility_data = CreateFacilitySchema(
                                name=facility.get("facility_name"),
                                sub_district_id=sub_district_id,
                                ownership=facility.get("ownership"),
                                facility_type=facility.get("facility_type"),
                                latitude=facility.get("latitude"),
                                longitude=facility.get("longitude"),
                                altitude=facility.get("altitude"),
                            )
                            try:
                                new_facility = facility_repository.create(data=new_facility_data)
                                print(f"{number}. Facility {new_facility.name} created.")
                            except ObjectAlreadyExistsException as e:
                                print(str(e), new_facility_data.name)
            print("DONE")
            print("\n")
        finally:
            db_session.close()

    print("CREATED LOCATIONS SUCCESSFULLY!")


if __name__ == "__main__":
    locations_file_path = os.path.join(os.path.dirname(__file__), "regions_districts_subdistricts_cleaned.json")
    create_locations(file_path=locations_file_path)
