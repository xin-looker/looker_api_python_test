import looker_sdk
from looker_sdk import models

sdk=looker_sdk.init31("looker.ini")


def soft_delete_look(id):
	sdk.update_look(look_id=id, body=models.WriteLookWithQuery(deleted=True))

soft_delete_look('252')