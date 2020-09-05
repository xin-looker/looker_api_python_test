import looker_sdk
from looker_sdk import models

sdk=looker_sdk.init31("looker.ini")

f={'users.gender': 'f'}

def create_new_query(query, filter):
	return models.WriteQuery(
		model=query.model,
        view=query.view,
        fields=query.fields,
        pivots=query.pivots,
        fill_fields=query.fill_fields,
        filters=filter,
        sorts=query.sorts,
        limit=query.limit,
        column_limit=query.column_limit,
        total=query.total,
        row_total=query.row_total,
        subtotals=query.subtotals,
        vis_config=query.vis_config,
        dynamic_fields=query.dynamic_fields,
        query_timezone=query.query_timezone,
		)

def update_look_filter(id):
	filter=sdk.look(id).query.filters
	filter.update(f)
	old_query=sdk.look(id).query

	new_query=sdk.create_query(body=create_new_query(old_query, filter))

	sdk.update_look(look_id=id, body=models.WriteLookWithQuery(query_id=new_query.id))


get_look_filter(210)
