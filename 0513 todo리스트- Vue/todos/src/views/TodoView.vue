<script setup>
import { onMounted } from 'vue'
import { usetodosStore } from '@/stores/counter'
import Todos from '@/components/Todos.vue'

const store = usetodosStore()

onMounted(() => {
  store.getTodos()
})
</script>

<template>
  <div>
    <h1>TODO</h1>
    <p v-for="todo in store.todos">{{ todo.title }} <br> {{ todo.content }}</p>
  </div>
</template>
