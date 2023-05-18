<template>
  <div id="app">
    <nav>
      <router-link to="/home"><img src="./assets/apple-logo.svg" class="logo"></router-link>
      <router-link to="/home">STILL</router-link>
      <form style="width:300px" class="form-group">
        <div class="form-group">
          <input type="text" class="form-control" style="width: 250px" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="button-addon2">
          <button class="btn btn-outline-secondary" type="button" id="button-addon2">Button</button>
        </div>
      </form>
      <router-link to="/create">CREATE</router-link>
      <router-link to="/login">LOG-IN</router-link>
      <router-link to="/user">MYPAGE</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.logo {
  height: 20px;
}

nav {
  padding: 0px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin-left : 10px;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<!-- <div id="searchBoxContainer" class="ujU wYR zI7 iyn Hsu" style="min-width: 407px;">
  <div class="Jea _HI fev zI7 iyn Hsu" style="height: 48px;">
    <div class="Jea KS5 XiG ujU zI7 iyn Hsu" style="padding: 0px 0px 0px 16px;height: 100%;">
      <div class="Eqh wc1 zI7 iyn Hsu">
        <svg class="gUZ ztu U9O kVc" height="16" width="16" viewBox="0 0 24 24" aria-label="검색 아이콘" role="img">
        <path d="M10 16c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6m13.12 2.88-4.26-4.26A9.842 9.842 0 0 0 20 10c0-5.52-4.48-10-10-10S0 4.48 0 10s4.48 10 10 10c1.67 0 3.24-.41 4.62-1.14l4.26 4.26a3 3 0 0 0 4.24 0 3 3 0 0 0 0-4.24"></path>
        </svg>
      </div>
      <div class="ujU zI7 iyn Hsu" style="height: 100%;">
        <input autocapitalize="off" autocorrect="off" autocomplete="off" aria-activedescendant="" aria-autocomplete="list" aria-controls="SuggestionsMenu" aria-describedby="searchBoxAccessibleText" aria-label="검색" aria-expanded="false" data-test-id="search-box-input" name="searchBoxInput" placeholder="검색" role="combobox" type="text" value="" style="background-color: transparent;border: none;color: rgb(51, 51, 51);font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen-Sans, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, &quot;ヒラギノ角ゴ Pro W3&quot;, &quot;Hiragino Kaku Gothic Pro&quot;, メイリオ, Meiryo, &quot;ＭＳ Ｐゴシック&quot;, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;font-size: 16px;font-weight: normal;height: 100%;outline: none;padding: 0px;width: 100%;">
        <div id="searchBoxAccessibleText" class="ESm zI7 iyn Hsu">
          자동 완성 결과를 이용할 수 있게 되면 위아래 화살표를 사용하여 결과를 확인하고 엔터를 눌러 선택하세요. 터치 디바이스 사용자는 터치하거나 손가락으로 밀어서 탐색하세요.
        </div>
      </div>
    </div>
  </div>
</div> -->