from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

projectslist = [
{
    'id': '1',
    'Project_Name' : 'e-commerce website',
    'Description' : 'This is the e-ecommerece wesite and makerting place to sell and buy products in online',
    'TopRated' :True
},
{
    'id' : '2',
    'Project_Name' : 'My Profile ',
    'Description' : 'A personal Website explain about the me and writing articles , blogs e.t.c',
    'TopRated' : False
},
{
    'id' : '3',
    'Project_Name' : 'Social Web app/ Website',
    'Description' : 'A website that done by social networking the people and connecting share ideas and views',
    'TopRated'    : True
}
]
    



def projects(request):
    projects = Project.objects.all()
    context1 = {'projects' :projects}
    return render(request,'projectweb/projectweb.html',context1)



def project(request,pk):
    projectObj =  Project.objects.get(id=pk)
    #tags       = projectObj.tags.all()
    #reviews    = projectObj.review_set.all()
    #reviews   = projectObj.reviews.all() # related name approach 
    contexts = {'project':projectObj}
    
    
    return render(request,'projectweb/singlepage.html',contexts)

def englishpage(request):
    name = "Ranga"
    age = 26
    context = {'name':name,'age':age}
    return render(request,'projectweb/englishphrases.html',context)

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
        #print("FORM DATA: ", request.POST)

    context = {'form':form}
    return render(request,'projectweb/project-form.html',context)

def updateProject(request,pk):
    context = {}
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    template = 'projectweb/project-form.html'
    if request.method == 'POST':
        form = ProjectForm(request.POST , instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    #context = {'form': form}
    context ["form"] = form
    return render(request,template,context)

def deleteProject(request,pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request,'projectweb/delete.html',{'object' : project})


















