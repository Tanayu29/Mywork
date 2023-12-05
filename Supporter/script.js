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
  