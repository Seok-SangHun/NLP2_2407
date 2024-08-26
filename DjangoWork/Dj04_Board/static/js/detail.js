// 문서 로딩이 끝나면 호출되는 함수 등록
window.onload = function(){
    document.getElementById('btnDel').addEventListener('click', function(){
        confirm("삭제하시겠습니까?") && document.forms['frmDelete'].submit();
    });
}