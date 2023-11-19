types_c_to_sql_type = {
    'string': 'nvarchar(50)',
    'bool': 'bit',
    'Boolean': 'bit',
    'int?': 'int',
    'int': 'int',
    
    'DateTime': 'Date',
    'Guid': 'uniqueidentifier ',
}

types_sql_to_c_type = {v: k for k, v in types_c_to_sql_type.items()}
types_sql_to_c_type["text"] : "string"

types_c_to_ts = {
    'string': 'string',
    'bool': 'boolean',
    'Boolean': 'boolean',
    'int?': 'number',
    'int': 'number',
    'Key': '',
    'DateTime': 'Date',
    'Guid': 'string',
    'TimingTypes': 'TimingTypes',
    'SendingTypes': 'SendingTypes',
    'TemplateTypes': 'TemplateTypes',
    'ICollection<TemplateCustomizationKey>': 'TemplateCustomizationKey []',
    'TemplateCustomizationKeyStatus': 'TemplateCustomizationKeyStatus',
    'ResourceImageItem': 'IResourceImageItem',
    'ResourceLink': 'IResourceLink'

}

g_unused_syntax = [';', '}', 'public', 'get', 'set', '{', 'const', '"']
annotations = {
    'DatabaseGenerated(DatabaseGeneratedOption.Identity)': 'identity',
    'Key': 'primary key'
}