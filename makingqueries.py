""" #Be sure import a model first before making queries
from inspect import Attribute
from turtle import title
from .models import ModelName

#all() - Retrieves all objects from a table
queryset = ModelName.objects.all()

#get(attribute = 'value') - Retrieve single object based on matched attribute
quertItem = ModelName.objects.get(attribute = 'value')

#filter(attribute = 'Value') - Returns all items from table that match a particular attribute
queryset = ModelName.object.filter(attribute='value')
                           .filter(attribute_startwith = 'value') # startwith char
                           .filter(attribute_contains = 'value')  # contains chars
                           .filter(attribute_icontains = 'value') # contains chars with case insensitive
                           .filter(attribute_gt = "value") # contains greater than value
                           .filter(attribute_gte = 'value') # contains greater than equal value
                           .filter(attribute_lt = 'value') # less than value
                           .filter(attribute_lte = 'value') # lessthan equal value
                        
#exculde(attribute = 'value') -Exculdes any object matching with that particular attribute

queryset = ModelName.object.exculde(attribute = 'value')

#order_by - Order a queryset by a particular attribute. Multiple parameters are allowed

queryset = Project.object.filter(title= "first project").order_by('value1','value2')

#order can be reversed by adding "-" before the attribute name
queryset = Project.object.filter(title="first Project").order_by('-value1','-value2')

#create() - create an instance of a model
item = ModelName.objects.create(attribute = 'value')

#save() - save changes made to a particular object
item = ModelName.objects.get(attribute = 'value')
item.title = "New Value"
item.save()

#delete() - Deletes a particular object
item = ModelName.objects.last()
item.delete()

#Query Models Children
item = ModelName.object.first()
item.childmodel_set.all()

#Query ManyToMany Fields
item  = ModelName.object.first()
item.relationshipname.all()

#Add ManyToMany Field
item = ModelName.object.first()
otheritem = OtherModule.objects.create(attribute = 'value')
item.relationshipname.add(otheritem)
























 """