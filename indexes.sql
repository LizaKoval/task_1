-- making up indexes --
create index bikes_inx on all_trips(bike_id);

create index mem_inx on trip_data(member_type);