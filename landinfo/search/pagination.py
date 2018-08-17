from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator, InvalidPage
#ページング機能
class paginate():
    #data:検索結果のデータ
    #request:コントロール側で受け取ったリクエストデータ
    def __init__(self, data, request):
        #検索結果を10レコード区切りで分割
        paginator = Paginator(data, 10)
        try:
        #GETリクエストで受け取ったページの変数を定義
            page_no = request.GET.get('page')
            self.page = paginator.page(page_no)
        except:
        #GETリクエストでページを受け取らなかった時の処理
            page_no = 1
            self.page = paginator.page(page_no)
        try:
        #カレントページの変数定義
            self.contacts = paginator.get_page(page_no)
        except (EmptyPage, PageNotAnInteger):
            self.contacts = paginator.page(1)