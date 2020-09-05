import looker_sdk
from looker_sdk import models

sdk=looker_sdk.init31("looker.ini")

def create_new_folder_give_edit_access(name, parent_id):
	if(sdk.search_folders(name=name, parent_id=parent_id)==[]):
		res=models.CreateFolder(name=name, parent_id=parent_id)
		this_folder=sdk.create_folder(body=res)
	else:
		this_folder=sdk.search_folders(name=name, parent_id=parent_id)[0]

	folder_metadata=sdk.content_metadata(content_metadata_id=this_folder.content_metadata_id)

	sdk.update_content_metadata(content_metadata_id=this_folder.content_metadata_id, body=models.WriteContentMeta(inherits=False))
	# sdk.create_content_metadata_access(body=models.ContentMetaGroupUser(content_metadata_id=this_folder.content_metadata_id, permission_type='edit', group_id='1'))

	sdk.update_content_metadata_access(content_metadata_access_id=sdk.all_content_metadata_accesses(content_metadata_id=this_folder.content_metadata_id)[0].id, body=models.ContentMetaGroupUser(content_metadata_id=this_folder.content_metadata_id, permission_type='edit', group_id='1'))


create_new_folder_give_edit_access('xin_created', '1')