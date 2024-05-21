<template>
    <div>
      <p>{{ comment.user.username }} - {{ comment.content }}</p>
      <v-btn
        class="mr-2"
        size="small"
        variant="tonal"
        color="green"
        @click="navigateToUpdateComment"
      >
        댓글 수정
      </v-btn>
      <v-btn
        class="mr-2"
        size="small"
        variant="tonal"
        color="red"
        @click="deleteComment"
      >
        댓글 삭제
      </v-btn>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useRouter, useRoute } from 'vue-router'
  import { useBoardStore } from '@/stores/counter'

  const store = useBoardStore()
  const route = useRoute()
  const props = defineProps({
    comment: Object
  })
  
  const router = useRouter()
  
  const navigateToUpdateComment = () => {
    router.push({ name: 'CommentUpdate', params: { commentId: props.comment.id } })
  }
  console.log(props)
  const deleteComment = () => {
    if (window.confirm('정말 삭제하시겠습니까?')) {
      axios({
        method: 'delete',
        url: `${store.API_URL}/community/article/${route.params.id}/comment/${props.comment.id}/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
        .then((response) => {
          console.log('댓글이 삭제됨!', response)
          router.go(0) // 현재 페이지 새로고침
        })
        .catch((error) => {
          console.log('댓글이 삭제되지 않았습니다.', error)
        })
    }
  }
  </script>
  
  <style scoped>
  /* 스타일 추가 */
  </style>
  