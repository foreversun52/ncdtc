from django.shortcuts import render
from main import models


# Create your views here.
def index(request):
    ncdc_list = models.NoncoRNA.objects.all()
    return render(request, 'index.html', locals())


def home(request):
    nonco_obj = models.NoncoRNA.objects
    ncrnd_id_list = nonco_obj.values('ncrna_name').distinct().order_by('ncrna_name')
    ncRNA_count = ncrnd_id_list.count()
    drug_id_list = nonco_obj.values('drug_name').distinct().order_by('drug_name')
    drug_count = drug_id_list.count()
    cancer_type_list = nonco_obj.values('cancer_type').distinct().order_by('cancer_type')
    cancer_count = cancer_type_list.count()
    return render(request, 'home/home.html', locals())


def bottom(request):
    return render(request, 'home/bottom.html')


def logo(request):
    return render(request, 'home/logo.html')


def menu(request):
    return render(request, 'home/menu.html')


def browse(request):
    nonco_obj = models.NoncoRNA.objects.all()
    ncrnd_id_list = nonco_obj.values('ncrna_id').distinct().order_by('ncrna_id')
    ncrnd_name_list = nonco_obj.values('ncrna_name').distinct().order_by('ncrna_name')
    drug_id_list = nonco_obj.values('drug_id').distinct().order_by('drug_id')
    drug_name_list = nonco_obj.values('drug_name').distinct().order_by('drug_name')
    cancer_type_list = nonco_obj.values('cancer_type').distinct().order_by('cancer_type')

    return render(request, 'browse.html', locals())


def browse_result(request, c_type):
    id = request.GET.get('id')
    nonco_obj = models.NoncoRNA.objects.all()
    if c_type == 'ncrna_id':
        back_data = nonco_obj.filter(ncrna_id=id)
    elif c_type == 'ncrna_name':
        back_data = nonco_obj.filter(ncrna_name=id)
    elif c_type == 'drug_id':
        back_data = nonco_obj.filter(drug_id=id)
    elif c_type == 'drug_name':
        back_data = nonco_obj.filter(drug_name=id)
    elif c_type == 'cancer_type':
        back_data = nonco_obj.filter(cancer_type=id)
    else:
        back_data = []
    return render(request, 'browse_result.html', locals())


def browse_result_details(request, id):
    if id:
        ncrnd_info = models.NoncoRNA.objects.filter(pk=id).first()
    return render(request, 'browse_result_details.html', locals())


def download(request):
    return render(request, 'download.html')


def help(request):
    return render(request, 'help.html')


def search(request):
    return render(request, 'search.html')


def search_by_ncrna(request):
    ncrnd_name_list = models.NoncoRNA.objects.values('ncrna_name').distinct().order_by('ncrna_name')
    return render(request, 'search/search_by_ncrna.html', locals())


def search_by_drug(request):
    drug_name_list = models.NoncoRNA.objects.values('drug_name').distinct().order_by('drug_name')
    return render(request, 'search/search_by_drug.html', locals())


def search_by_cancer(request):
    cancer_type_list = models.NoncoRNA.objects.values('cancer_type').distinct().order_by('cancer_type')
    return render(request, 'search/search_by_cancer.html', locals())


def search_result(request, key):
    noncoRNA_obj = models.NoncoRNA.objects
    if key == 'ncRNA':
        values = request.GET.get('ncRNA', '')
        search_results = noncoRNA_obj.filter(ncrna_name__icontains=values)
    elif key == 'drug':
        values = request.GET.get('drug', '')
        search_results = noncoRNA_obj.filter(drug_name__icontains=values)
    elif key == 'cancer':
        values = request.GET.get('cancer', '')
        search_results = noncoRNA_obj.filter(cancer_type__icontains=values)
    else:
        search_results = []
    return render(request, 'search/search_result.html', locals())


def search_result_details(request, id):
    if id:
        ncrnd_info = models.NoncoRNA.objects.filter(pk=id).first()
    return render(request, 'search/search_result_details.html', locals())


def submit(request):
    if request.method == 'POST':
        ncRNA_name = request.POST.get('ncRNA_name', '')
        ncRNA_id = request.POST.get('ncRNA_id', '')
        disease = request.POST.get('disease', '')
        drug_name = request.POST.get('drug_name', '')
        drug_id = request.POST.get('drug_id', '')
        drug_response = request.POST.get('drug_response', '')
        expression_pattern = request.POST.get('expression_pattern', '')
        pmid = request.POST.get('pmid', '')
        email = request.POST.get('email', '')
        description = request.POST.get('description', '')
        if ncRNA_name and ncRNA_id and disease and expression_pattern and pmid and email and description:
            submit_obj = models.Submit.objects.create(ncRNA_Name=ncRNA_name, ncRNA_ID=ncRNA_id, Disease=disease, Drug_Name=drug_name, Drug_ID=drug_id, Drug_Response=drug_response, Description=description, Expression_pattern=expression_pattern, PubMed_ID=pmid, Email=email)
            if submit_obj:
                back_msg = 1
            else:
                back_msg = 0
    return render(request, 'submit.html', locals())
