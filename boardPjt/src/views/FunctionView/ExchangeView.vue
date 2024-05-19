<template>
  <div>
    <button @click="fetchExchangeData">Fetch Exchange Data</button>
    <div v-if="loading">Loading...</div>
    <div v-if="error">{{ error }}</div>
    <div v-if="exchangeData">
      <h3>Exchange Data</h3>
      <pre>{{ exchangeData }}</pre>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      exchangeData: null,
      loading: false,
      error: null,
    };
  },
  methods: {
    async fetchExchangeData() {
      this.loading = true;
      this.error = null;
      try {
        const response = await axios.get('http://127.0.0.1:8000/exchange');
        this.exchangeData = response.data;
      } catch (error) {
        if (error.response) {
          this.error = `Error: ${error.response.status} - ${error.response.data}`;
        } else {
          this.error = `Error: ${error.message}`;
        }
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style>
/* Add your styles here */
</style>
