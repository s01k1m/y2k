<template>
  <div class="create">
    <h1>스틸컷을 크리에이트하는 포스팅 페이지입니다. ^^</h1>
    <form>
      <v-file-input v-model="files" :multiple="false" placeholder="파일찾기" label="File input" :show-size="1000">d</v-file-input>
      <!-- 여러파일 보낼경우 multiple 사용 -->
      <button @click="sendImages">submit</button>
    </form>
    
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      image: null,
      movie_id: null,
      files: null,
    }
  },
  computed: {
    isLogin() {
      return localStorage.getItem("access_token")
    }
  },
  created() {
    this.isLogined()
  },
  methods: {
    isLogined() {
      if (!this.isLogin) {
        console.log('if')
        alert('로그인이 필요합니다.')
        this.$router.push({ name: 'login' })
      } 
    },
    // image 보내기
    sendImages(e) {
      e.preventDefault()
      console.log('sendImages 실행합니다.')
      let info = new FormData()
      // info.append('files', this.files)
      info.files = this.files
      if (this.files===null) {             // 파일을 보내지 않을 경우
        info.append('files', [])
      } else {
        console.log(
          '파일은 있음'
        )
        // info.append('files', this.files)

        // for (let i = 0; i < this.files.length; i++) {   // 파일이 하나 이상인 경우
        //   info.append('files', this.files[i]);
        // }
      }
      console.log('info: ', info)
      console.log('files: ', this.files)
      const token = localStorage.getItem("token") // token을 세션에 저장시켜 사용했기 때문에
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data', // Content-Type을 변경해야 파일이 전송됨
          'Authorization': `token ${token}`,
          'Access-Control-Allow-Origin':'http://127.0.0.1:8000/'
          }
      }
      console.log(info)
      axios.post(
        'http://127.0.0.1:8000/', 
        info, config)
      .then((res) => {
        console.log('데이터를 http://127.0.0.1:8000/create/로 보내고 있음')
        console.log(res) // 필요한 것 넣어서 쓰면됨
      })
    }
  }
}
</script>

<style>
#create {
  margin: 24px;
}

</style>