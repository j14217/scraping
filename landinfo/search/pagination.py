from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator,InvalidPage

class paginate():

    def __init__(self,data,request):
        paginator = Paginator(data, 10)
        try:
            page_no = request.GET.get('page')
            self.page = paginator.page(page_no)
        except:
            page_no = 1
            self.page = paginator.page(page_no)
        try:
            self.contacts = paginator.get_page(page_no)
        except (EmptyPage, PageNotAnInteger):
            self.contacts = paginator.page(1)

    def get_countact(self):
        return self.contacts

    def get_page(self):
        return self.page
    