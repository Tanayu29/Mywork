function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
  
    // すべてのタブコンテンツを非表示にする
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // すべてのタブリンクのアクティブ状態を解除する
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // クリックされたタブをアクティブにし、関連するコンテンツを表示する
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }
  
  // 初期表示時に最初のタブをアクティブにする
  document.getElementsByClassName("tablinks")[0].click();
  
function runLogSummarize1() {
  // Log.pyを実行するためのサーバーサイドのエンドポイントにリクエストを送信
  fetch('/run-log-summarize1', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
      console.log('Log.py 実行結果:', data);
      // 必要に応じて結果を処理
    })
    .catch(error => {
      console.error('エラー:', error);
    });
}

function runLogSummarize2() {
  // "ログ集計.xlsm"を開くためのサーバーサイドのエンドポイントにリクエストを送信
  window.open('/open-log-summarize2');
}
