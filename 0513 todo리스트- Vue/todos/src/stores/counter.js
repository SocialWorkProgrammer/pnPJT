import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const usetodosStore = defineStore('todos', () => {
  const todos = ref([])
  const API_URL = 'http://70.12.102.167:5173'

  const getTodos = function () {
    axios({
      method : 'get',
      url : `${API_URL}/todolist/`
    })
    .then((response) => {
      console.log(response)
      todos.value = response.data
    })
    .catch((error) =>
      console.log('좢됐어!!', error))
  }

  return { todos, API_URL, getTodos }
}, {persist:true})
