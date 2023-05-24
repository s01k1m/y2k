<template>
  <div>
    <div id="container">
      <div id="commentfooter">
        <input type="text" @keyup.enter="commentSubmit(comment_id)" v-model="comment_content">
      </div>
      <div v-for="(comment, index) in child_comment_list" :key="index">
        <div id="commentcontainer">
          <div id="commentbody">
            <span id="userid">
              {{ comment.username }}  
            </span>
            <span id="content">
              {{ comment.content }}
            </span>
          </div>
          <div>
            <button id="deletebutton" @click="deleteComment(comment.id)">X</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: 'ChildComment',
  props: {
    child_comment_list: Array,
    comment_id: Number,
    still_id: Number
  },
  data() {
    return {
      comment_content: null,
    }
  },
  methods: {
    emitToParent() {
      this.$emit('child-comment-submit')
    },
    commentSubmit(comment_id) {
      if (!this.comment_content) {
        alert('내용을 입력하세요.')
      } else {
        let token = localStorage.getItem("access_token")
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/communities/${this.still_id}/`,
          data: {
            'content': this.comment_content,
            'parent': comment_id,
          },
          headers: {
              Authorization: "Token " + token,
          },
        })
        .then((response) => {
          console.log('대댓글 작성 성공', response)
          this.comment_content = ''
          this.emitToParent()
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    deleteComment(id) {
      let token = localStorage.getItem("access_token")
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/communities/${id}/delete/`,
        headers: {
          Authorization: "Token " + token,
        },
      })
      .then((response) => {
        console.log('삭제 성공: ', response)
        this.emitToParent()
      })
      .catch(() => {
        alert('본인이 작성한 댓글만 삭제할 수 있습니다.')
      })
    },
  }
}
</script>

<style scoped>
#container {
  display: flex;
  flex-direction: column;
  text-align: left;
  justify-content: space-between;
  padding-left: 20px;
}
#userid {
  font-weight: 600;
  text-align: left;
  font-size: 18px;
  margin-right: 5px;
}
#content {
  text-align: left;
  font-weight: 400;
  font-size: 16px;
}
#commentcontainer {
  margin: 2px 5px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
#commentbody {
  justify-content: space-between;
  flex-direction: row;
}
#commentfooter {
  height: 48px;
  border: solid 1px #e9e9e9;
  border-radius: 24px;
  padding: 1px 2px;
  background-color: white;
  display: inline;
  padding: 0 20px;
  flex: 3;
  text-align: left;
}
#deletebutton {
  width: 20px;
}
#create {
  font-weight: 400;
  font-size: 16px;
}
</style>