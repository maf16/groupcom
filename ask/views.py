from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Question
from .forms import NameForm
from .models import Question


def post_question(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # if form is valid...
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # database query choosing top 3  questions
            suggested_questions = suggest_questions()

            # if question in database, iterate question_occurance, else save question to database
            obj, created = Question.objects.get_or_create(question_text = form.cleaned_data['query'])
            Question.objects.filter(question_text = form.cleaned_data['query']).update(question_occurrence = obj.question_occurrence + 1)
            context = {
                'last_question': form.cleaned_data['query'],
                'suggested_questions': suggested_questions
            }
            return render(request, 'ask/suggest_questions.html', context)
    else:
        form = NameForm()
    return render(request, 'ask/index.html', {'form': form})


def suggest_questions():
    """
    Investigates the Question object in the database and makes three suggested questions
    :return: top 3 suggested questions as a dict of style {0:top question, 1:second question, ...}
    """
    suggested_questions = {}
    dataset = Question.objects.order_by('question_occurrence').reverse()
    for i in dataset[0:3]:
        suggested_questions[len(suggested_questions)] = i
    while len(suggested_questions) < 3:
        suggested_questions[len(suggested_questions)] = "None"

    return suggested_questions


def compose_answer(request):
    return render(request, 'ask/answer.html')


def choose_question(request):
    for i in Question.objects.all():
        print(i)
    context = {
        'all_questions':Question.objects.all(),
    }

    return render(request, 'ask/choose_question_to_answer.html',context)


def barchart(request):
    # instantiate a drawing object
    from .mycharts import MyBarChartDrawing
    d = MyBarChartDrawing()

    # extract the request params of interest.
    # I suggest having a default for everything.
    if 'height' in request:
        d.height = int(request['height'])
    if 'width' in request:
        d.width = int(request['width'])

    if 'numbers' in request:
        strNumbers = request['numbers']
        numbers = map(int, strNumbers.split(','))
        d.chart.data = [numbers]  # bar charts take a list-of-lists for data

    if 'title' in request:
        d.title.text = request['title']

    # get a GIF (or PNG, JPG, or whatever)
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')