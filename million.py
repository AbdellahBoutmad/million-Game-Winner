from tkinter import *
import ttkbootstrap as tb

questions = [
    {
        "question": "ما هي عاصمة فرنسا؟",
        "answers": ["باريس", "لندن", "روما"],
        "correct_answer": "باريس"
    },
    {
        "question": "ما هو لون السماء؟",
        "answers": ["أزرق", "أحمر", "أخضر"],
        "correct_answer": "أزرق"
    },
    {
        "question": "ما الحيوان الذي يطير؟",
        "answers": [ "الجمل","الخروف", "عصفور"],
        "correct_answer": "الجمل"
    },
    {
        "question": "من هو أول رئيس للولايات المتحدة الأمريكية؟",
        "answers": [ "جون آدمز","جورج واشنطن","توماس جيفرسون"],
        "correct_answer": "جورج واشنطن"
    },
    {
        "question": "ما هي عاصمة روسيا؟",
        "answers": ["موسكو", "سانت بطرسبرغ", "نوفوسيبيرسك"],
        "correct_answer": "موسكو"
    },
    {
        "question": "ما هو أكبر نهر في العالم؟",
        "answers": ["النيل", "الأمازون", "اليانغتسي"],
        "correct_answer": "الأمازون"
    },
    {
        "question": "ما هي عاصمة إيطاليا؟",
        "answers": ["روما", "ميلانو", "فلورنسا"],
        "correct_answer": "روما"
    },
    {
        "question": "ما هو عدد الدول الأعضاء في الاتحاد الأوروبي؟",
        "answers": ["27", "28", "29"],
        "correct_answer": "27"
    },
    {
        "question": "ما هي عاصمة تركيا؟",
        "answers": ["أنقرة", "اسطنبول", "أزمير"],
        "correct_answer": "أنقرة"
    },
    {
        "question": "ما هي عاصمة الهند؟",
        "answers": ["مومباي","نيودلهي",  "كولكاتا"],
        "correct_answer": "نيودلهي"
    },
    {
        "question": "ما هو عدد كواكب المجموعة الشمسية؟",
        "answers": ["10","8", "9" ],
        "correct_answer": "8"
    },
    {
        "question": "ما هي عاصمة الصين؟",
        "answers": ["بكين", "كانتون", "شنغهاي"],
        "correct_answer": "بكين"
    },
    {
        "question": "ما هو أكبر قارة في العالم؟",
        "answers": ["آسيا", "أفريقيا", "أمريكا الشمالية"],
        "correct_answer": "آسيا"
    },
    {
        "question": "ما هو أكبر محيط في العالم؟",
        "answers": [ "الهندي","الهادئ", "الأطلسي"],
        "correct_answer": "الهادئ"
    },
    {
        "question": "ما هو أكبر بحيرة في العالم؟",
        "answers": ["بحيرة السد العالي", "بحيرة فيكتوريا", "بحيرة البايكال"],
        "correct_answer": "بحيرة السد العالي"
    },
    {
        "question": "ما هو أكبر جبل في العالم؟",
        "answers": ["إفرست", "كليمنجارو", "ك2"],
        "correct_answer": "إفرست"
    },
    {
        "question": "ما هو أكبر حيوان على وجه الأرض؟",
        "answers": ["الحوت الأزرق", "الفيل الأفريقي", "الدب الروسي"],
        "correct_answer": "الحوت الأزرق"
    },
    {
        "question": "ما هي عاصمة ألمانيا؟",
        "answers": ["برلين", "ميونخ", "هامبورغ"],
        "correct_answer": "برلين"
    },
    {
        "question": "ما هو عدد أيام الأسبوع؟",
        "answers": ["7", "8", "6"],
        "correct_answer": "7"
    },
    {
        "question": "ما هو عدد أركان الإسلام؟",
        "answers": ["5", "6", "7"],
        "correct_answer": "5"
    },
    {
        "question": "ما هي عاصمة اليابان؟",
        "answers": ["طوكيو", "أوساكا", "كيوتو"],
        "correct_answer": "طوكيو"
    },
    {
        "question": "ما هو عاصمة البرازيل؟",
        "answers": ["برازيليا", "ريو دي جانيرو", "ساو باولو"],
        "correct_answer": "برازيليا"
    },
    {
        "question": "ما هو أكبر دولة في العالم من حيث المساحة؟",
        "answers": ["روسيا", "كندا", "الصين"],
        "correct_answer": "روسيا"
    },
    {
        "question": "ما هي عاصمة الهند؟",
        "answers": ["نيودلهي", "مومباي", "كولكاتا"],
        "correct_answer": "نيودلهي"
    },
    {
        "question": "ما هي عاصمة كندا؟",
        "answers": ["أوتاوا", "تورونتو", "فانكوفر"],
        "correct_answer": "أوتاوا"
    },
    {
        "question": "ما هو عاصمة أستراليا؟",
        "answers": ["كانبرا", "سيدني", "ملبورن"],
        "correct_answer": "كانبرا"
    },
    {
        "question": "ما هو عاصمة سويسرا؟",
        "answers": ["برن", "جنيف", "زيورخ"],
        "correct_answer": "برن"
    },
    {
        "question": "ما هي عاصمة النمسا؟",
        "answers": ["فيينا", "سالزبورغ", "غراتس"],
        "correct_answer": "فيينا"
    },
    {
        "question": "ما هي عاصمة هولندا؟",
        "answers": ["أمستردام", "روتردام", "لاهاي"],
        "correct_answer": "أمستردام"
    },
    {
        "question": "ما هي عاصمة السويد؟",
        "answers": ["ستوكهولم", "مالمو", "جوتنبرغ"],
        "correct_answer": "ستوكهولم"
    },
    {
        "question": "ما هي عاصمة النرويج؟",
        "answers": ["أوسلو", "برغن", "ستافانغر"],
        "correct_answer": "أوسلو"
    },
    {
        "question": "ما هي عاصمة الدنمارك؟",
        "answers": ["كوبنهاجن", "أودنس", "آلبورغ"],
        "correct_answer": "كوبنهاجن"
    },
    {
        "question": "ما هي عاصمة فنلندا؟",
        "answers": ["هلسنكي", "تامبيري", "إسبو"],
        "correct_answer": "هلسنكي"
    },
    {
        "question": "ما هي عاصمة بولندا؟",
        "answers": ["وارسو", "كراكوف", "لودز"],
        "correct_answer": "وارسو"
    },
    {
        "question": "ما هي عاصمة بلجيكا؟",
        "answers": ["بروكسل", "أنتويرب", "جنت"],
        "correct_answer": "بروكسل"
    },
    {
        "question": "ما هي عاصمة إسبانيا؟",
        "answers": ["مدريد", "برشلونة", "فالنسيا"],
        "correct_answer": "مدريد"
    },
]  
home = tb.Window(themename="solar")
home.geometry("400x400")
home.title("من سيربح الدرهم")

question_afficher = 0




def check(answer_index):
    global question_afficher
    user_answer = questions[question_afficher]["answers"][answer_index]
    correct_answer = questions[question_afficher]["correct_answer"]
    
    if user_answer == correct_answer:
      
        question_afficher += 1

        if question_afficher < len(questions):
            show_question()
        else:
            mil=Label(home,text=" مبروك عليك مليون دوز تاخد شيك",font="Helevetica 20")
            mil.pack()
            exit
    else:
       
        for i in range(3):
            answer_buttons[i].configure(style="danger.Outline.TButton")
        answer_buttons[questions[question_afficher]["answers"].index(correct_answer)].configure(style="success.Outline.TButton")

def show_question():
    question_label.config(text=questions[question_afficher]["question"])
    for i in range(3):
        answer_buttons[i].config(text=questions[question_afficher]["answers"][i], style="success.Outline.TButton")

question_label = Label(home, font="Helvetica 20")
question_label.pack()

answer_buttons = []
for i in range(3):
    button = tb.Button(home, text=f"{i+1}", style="success.Outline.TButton", command=lambda i=i: check(i))
    button.pack(pady=20, ipadx=40, ipady=6)
    answer_buttons.append(button)

show_question()
home.mainloop()
