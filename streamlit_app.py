# from dotenv import load_dotenv
# load_dotenv()

#from langchain.llms import OpenAI
from langchain_openai import OpenAI

llm =OpenAI()
result=llm.predict("내가 좋아하는 동물은");

from langchain_openai.chat_models import ChatOpenAI
chat_model=ChatOpenAI()
chat_model.predict("hi~");


#from langchain.chat_models  import ChatOpenAI
#from langchain_openai import OpenAI, ChatOpenAI



#chat_model=ChatOpenAI()

#result=llm.predict("hi!")
#llm.predict("hi!")
#chat_model.predict("hi!")


import streamlit as st

st.title("초등학교 서술형 평가 문항 인공지능 자동 채점 서비스 개발 및 적용")
st.title("주관식 평가 chatgpt test 시작 ")

student_grade = st.text_input('평가 학년 ex)초등학교 5학년', '')

student_input = st.text_input('평가 항목을 입력하세요 ex)만보는 늦둥이로 태어난 아이었어. 만가지 보물이라는 이름을 가진 아이였지. 하지만, 용기가 조금 부족했어. 겁이 너무 많았어. 특히 학교에 가는 것을 가장 힘들어 했어. 학교에서는 작은 일에도 깜짝 놀라는 아이었지. 그래서 학교 친구들은 만보를 '"겁보"'라고 놀렸어. \n 그래서 만보의 부모님은 만보를 용기있게 만들기 위해 바깥심부름을 시키기로 했어.', '')

#st.write('평가항목은', student_input)
standard_5year = st.text_input('평가 기준을  입력하세요 ex)상: 인물의 특징, 인상 깊은 말이나 행동, 칭찬할 점과 고칠 점, 해 주고 싶은 말을 모두 적절하게 씀 중: 인물의 특징, 인상 깊은 말이나 행동, 칭찬할 점과 고칠 점, 해 주고 싶은 말 중 일부를 적절하게 씀   하: 인물의 특징, 인상 깊은말이나 행동, 칭찬할 점과 고칠 점, 해 주고싶은 말 중 일부를 씀', '')
#st.write('평가기준은\n', standard_5year+ "\n 입니다.")
#st.title("GPT 연계 테스트를 위한 기본값 입력 ")
#if st.button('평가 학년, 평가항모그, 평가기준을  기본 입력  합니다.'):
#    st.write('초등학교 5학년', student_grade)
#    st.write('상: 인물의 특징, 인상 깊은 말이나 행동, 칭찬할 점과 고칠 점, 해 주고 싶은 말을 모두 적절하게 씀 중: 인물의 특징, 인상 깊은 말이나 행동, 칭찬할 점과 고칠 점, 해 주고 싶은 말 중 일부를 적절하게 씀   하: 인물의 특징, 인상 깊은말이나 행동, 칭찬할 점과 고칠 점, 해 주고싶은 말 중 일부를 씀', standard_5year)
#    st.write('만보는 늦둥이로 태어난 아이었어. 만가지 보물이라는 이름을 가진 아이였지. 하지만, 용기가 조금 부족했어. 겁이 너무 많았어. 특히 학교에 가는 것을 가장 힘들어 했어. 학교에서는 작은 일에도 깜짝 놀라는 아이었지. 그래서 학교 친구들은 만보를 '"겁보"'라고 놀렸어. \n 그래서 만보의 부모님은 만보를 용기있게 만들기 위해 바깥심부름을 시키기로 했어.', student_input)


def check_input(arg_data, arg_title):
    if arg_data:  # 사용자가 어떤 값을 입력했다면
        st.success(f"환영합니다, {arg_data}!")  # 환영 메시지 출력
    else:
        st.error(f"{arg_title}!")  # 올바른 에러 메시지 출력
        return  # 입력값이 없으므로 여기서 함수 종료


st.title("버튼을 클릭하세요. GPT와 연결합니다. ")
# check_input(standard_5year,'평가기준')
# check_input(student_input,'평가데이터')
# check_input(student_grade,'평가학년')



if st.button('평가 학년, 평가항목, 평가기준을 입력 후 클릭하면 GPT3.5 연계하여 평가를 시작합니다..'):
    #st.write('평가기준은', standard_5year+standard_5year+"평가를 해줘")
    input_value="나는 "+student_grade+" 선생님이야. 이 내용은 초등학생에게 보여줄 내용이야.! ##평가기준##\n"+standard_5year + "##학생입력값##:\n"+student_input +" ##작업 ##  평가결과 먼저 보여줘. 이후 한줄 간격을 두고 학생 입력값을 평가기준에 따라 평가의견을 작성하고, 한줄 간격을 두고 고칠 내용도 같이 작성해줘. "
    result=chat_model.predict(input_value)
    print("\n\n")
    print(input_value)
    print("\n\n")
    print("GPT답변 값:"+result)
    st.write("GPT답변:\n\n "+result)



# import pandas as pd
# from io import StringIO

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

#     # To convert to a string based IO:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)

#     # To read file as string:
#     string_data = stringio.read()
#     st.write("string_data"+string_data)

#     # Can be used wherever a "file-like" object is accepted:
#     dataframe = pd.read_csv(uploaded_file)
#     st.write("dataframe"+dataframe)



# st.title("#######################")
# #st.title("내가 좋아하는 동물은")
# #st.title(result)
# st.title("샘플 예시")
# st.write('평가항목:\n만보는 늦둥이로 태어난 아이었어. 만가지 보물이라는 이름을 가진 아이였지. 하지만, 용기가 조금 부족했어. 겁이 너무 많았어. 특히 학교에 가는 것을 가장 힘들어 했어. 학교에서는 작은 일에도 깜짝 놀라는 아이었지. 그래서 학교 친구들은 만보를 '"겁보"'라고 놀렸어. \n 그래서 만보의 부모님은 만보를 용기있게 만들기 위해 바깥심부름을 시키기로 했어.')
# st.write('평가 기준:\n상: 인물의 특징, 인상 깊은 말이나 행동, 칭찬할 점과 고칠 점, 해 주고 싶은 말을 모두 적절하게 씀'+
#                     '\n중: 인물의 특징, 인상 깊은 말이나 행동, 칭찬할 점과 고칠 점, 해 주고 싶은 말 중 일부를 적절하게 씀'+
#                     '\n하: 인물의 특징, 인상 깊은말이나 행동, 칭찬할 점과 고칠 점, 해 주고싶은 말 중 일부를 씀')


# st.write('GPT답변 값:만보는 늦둥이로 태어나서 용기가 조금 부족한 아이였지만, 그에도 불구하고 자신의 부족함을 극복하기 위 해 노력하는 모습이 인상 깊었어요. 특히 학교에 가는 것을 꺼리는 만보가 부모님의 도움으로 바깥심부름을 하면서 용 기를 키워나가는 모습은 칭찬할 만한 점이에요. 만보는 겁보라는 비아냥거림에도 굴하지 않고 자신의 부족함을 극복하 려 노력했어요.\n' +
#          '고쳐야 할 점은 만보가 겁을 많이 먹어서 작은 일에도 깜짝 놀라는 습관을 고칠 필요가 있어요. 조금 더 자신을 믿고  용기를 내어 두려움을 극복해 나가면 좋을 것 같아요.'+
#          '등급: 중 \n ##모델답안##'+
#           '만보는 늦둥이로 태어난 아이이며, 용기가 부족한 편이었습니다. 학교에 가는 것을 꺼리고 작은 일에도 쉽게 놀라는 경향이 있었죠. 그러나 부모님의 도움으로 바깥심부름을 하면서 자신을 꾸준히 극복해 나가는 모습은 참 인상 깊었습니다. 겁보라는 비아냥거림에도 굴하지 않고 자신을 믿고 노력하는 만보의 모습은 칭찬할 만한 점이에요.'+
#           '하지만 만보는 여전히 겁을 많이 먹어 작은 일에도 쉽게 놀라는 습관이 있습니다. 좀 더 자신을 믿고 용기를 내어 두려움을 극복해 나가는 노력이 필요할 것 같아요.')

#print(result)



#st.button("평가해주세요", type="primary")


