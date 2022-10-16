import httpx
import streamlit as st
 
 
def view_response(res):
    '''検索クエリ結果の表示'''
    # ステータスチェック
    if res["response"]["status"] != 0:
        st.error("検索中に問題が発生しました。管理者にご相談ください。")
 
    # 検索ヒット件数
    record_count = res["response"]["record_count"]
 
    # 検索ワード
    q = res["response"]["q"]
 
    if record_count == 0:
        # 検索結果がない場合
        st.error(f'{q}に一致する情報は見つかりませんでした。')
    else:
        # 検索件数など
        page_number = res["response"]["page_number"]
        startRange = res["response"]["start_record_number"]
        endRange = res["response"]["end_record_number"]
        exec_time = res["response"]["exec_time"]
        # "q" の検索結果 232 件中 1 - 10 件目 (0.2 秒)
        st.write(
            f" **{q}** の検索結果 **{record_count}** 件中 **{startRange} - {endRange}** 件目 ({exec_time}秒)")
 
        # 検索結果表示処理
        results = res["response"]["result"]
        for i, result in enumerate(results):
            # 検索結果
            title = result["title"]
            url_link = result["url_link"]
            digest = result["digest"]
            st.markdown(f"#### {i+1}. [{title}]({url_link})",
                        unsafe_allow_html=True)
            st.markdown("")  # 改行
            st.markdown(digest)
 
        # nページ目
        st.markdown(f"{page_number}ページ目")
 
        return page_number, endRange
 
 
def query_ui():
    '''検索クエリ用UI'''
    # 検索ワード入力
    input_word = st.text_input(label='キーワード入力', value='')
    st.write(f'検索ワード: {input_word}')
 
    # 検索件数
    page_size = st.sidebar.number_input(label='件数', value=10, step=10)
    st.sidebar.write(f'件数: {page_size}')
 
    # 開始する件数位置
    start_record_number = st.sidebar.number_input(
        label='開始する件数位置', value=0, step=10)
    st.sidebar.write(f'開始する件数位置: {start_record_number}')
 
    return input_word, page_size, start_record_number
 
 
def main():
    '''全文検索アプリ'''
    # アプリ名
    st.markdown('## 全文検索アプリ')
 
    # 検索クエリ
    input_word, page_size, start_record_number = query_ui()
 
    # 検索
    if st.button("検索"):
        # GETリクエスト
        response = httpx.get(
            f'http://localhost:8080/json/?q={input_word}&num={page_size}&start={start_record_number}')
        # response = requests.get(
        #     f'http://localhost:8080/json/?q={input_word}&num={page_size}&start={start_record_number}')
 
        # 検索結果をJSONで受け取る
        res = response.json()
 
        # 検索結果の表示処理
        view_response(res)
 
        # 検索結果詳細
        with st.expander("検索結果詳細 for debug"):
            st.json(res)
 
 
if __name__ == '__main__':
    main()
 