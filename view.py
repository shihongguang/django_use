from django.http.response import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage


def instance(*_cls_args):

    def _init_wrapper(cls):

        _instance_obj = cls()

        if _cls_args:
            for init_args in _cls_args:
                _instance_obj = init_args(_instance_obj)

        def _cls_instance(*args, **kwargs):

            try:
                return _instance_obj(*args, **kwargs)
            except ObjectDoesNotExist:
                return Http404

        return _cls_instance
    return _init_wrapper


class View(object):

    def __init__(self):
        self.HttpResponse = HttpResponse
        self.render = render
        self.redirect = redirect

        self.p = None

    def __call__(self, request, *args, **kwargs):
        self.request = request

        if request.method == "GET":
            return self.get()
        elif request.method == "POST":
            return self.post()
        else:
            return self._http_405

    @property
    def request_args(self):
        return self.request.GET

    @property
    def request_body(self):
        return self.request.POST

    def get(self):
        return self._http_405

    def post(self):
        return self._http_405

    @property
    def _http_405(self):
        return HttpResponse(status=405)

    @property
    def offset(self, offset_num=1):
        return int(self.request_args.get("offset", offset_num))

    @property
    def limit(self, limit_num=100):
        return int(self.request_args.get("limit", limit_num))

    def query_sets(self, query_set):
        self.p = Paginator(query_set, self.offset)

        try:
            result_page = self.p.page(self.limit)
        except EmptyPage:
            result_page = self.p.page(self.p.num_pages)

        return result_page
