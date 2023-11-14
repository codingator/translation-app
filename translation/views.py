from django.http import HttpResponse
from django.template import loader
from .forms import TranslationForm
import deepl
import os

# Create your views here.


def index(request):
    """
    翻訳画面
    """

    #　翻訳結果
    translation_results = ""

    if request.method == "POST":
        # 翻訳ボタン押した時

        form = TranslationForm(request.POST)

        # バリデーションチェック

        if form.is_valid():
            # 翻訳
            # TODO: 認証キーのハードコーディングは避ける
            translator = deepl.Translator(os.getenv('DEEPL_AUTH_KEY'))

            # 翻訳文を取得
            sentence  = form.cleaned_data['sentence']

            # 日本語に翻訳
            translation_results = translator.translate_text(
                sentence,target_lang="EN-US"
            )
            pass

    else:
        form = TranslationForm()

    template = loader.get_template(r'translation/Index.html')
    context = {
        'form': form,
        'translation_results':translation_results
    }
    return HttpResponse(template.render(context,request))
