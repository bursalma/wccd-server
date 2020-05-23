# if not last_name or not first_name:
#     unmet_response = {
#         'error'  : 'requirements unmet',
#         'message': 'last_name and first_name fields are required'}
#     return unmet_response, 404

# existing_convict = Convict.query.filter(
#     Convict.last_name == last_name).filter(
#     Convict.first_name == first_name).first()

# if existing_convict:
#     exists_response = {
#         'error'  : 'record exists',
#         'message': f'{last_name}, {first_name} already exists'}
#     return exists_response, 404