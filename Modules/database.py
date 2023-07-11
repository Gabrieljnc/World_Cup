import matches
import events
from sqlalchemy import create_engine

connection_path = 'postgresql://1922120013_TCC_Gabriel:1922120013_TCC_Gabriel@18.224.151.110/IESB_Soccer_Performance'
conn_string = connection_path

engine = create_engine(conn_string)

with engine.connect() as conn:
    schema_name = "public"  

    for id, df in (events.frames.items()):
        table_name = f"Match_{id}"
        df.to_sql(table_name, con=conn, if_exists="replace", index=False, schema=schema_name)

    events.all_data_events.to_sql('All_events_data', con=conn, if_exists="replace", index=False, schema=schema_name)
    matches.all_matches.to_sql('All_matches_detail', con=conn, if_exists="replace", index=False, schema=schema_name)


