from astra.db_api_client import database_connection
from astrapy.info import (
    CreateTableDefinition,
    ColumnType,
    TablePrimaryKeyDescriptor,
    TableScalarColumnTypeDescriptor

)


def create_table():
    db = database_connection()

    table_definition = CreateTableDefinition(
        columns = {
            "id" : TableScalarColumnTypeDescriptor(
                column_type=ColumnType.UUID
            ),
            "timestamp" : TableScalarColumnTypeDescriptor(
                column_type=ColumnType.TEXT
            ),
            "city" : TableScalarColumnTypeDescriptor(
                column_type = ColumnType.TEXT
            ),
            "country" : TableScalarColumnTypeDescriptor(
                column_type = ColumnType.TEXT
            ),

            "temperature" : TableScalarColumnTypeDescriptor(
                column_type = ColumnType.FLOAT
            ),
            "pressure" : TableScalarColumnTypeDescriptor(
                column_type = ColumnType.FLOAT
            ),

            "humidity" : TableScalarColumnTypeDescriptor(
                column_type = ColumnType.FLOAT
            ),
            "wind_speed" : TableScalarColumnTypeDescriptor(
                column_type = ColumnType.FLOAT
            )
        },

        primary_key = TablePrimaryKeyDescriptor(
            partition_by = ["id"], partition_sort = {}
        )
    )

    if "cities_weather" not in db.list_table_names():
        db.create_table("cities_weather", definition=table_definition)
        print("Table created Suceessfully!")
    else:
        print("The table already exits!")