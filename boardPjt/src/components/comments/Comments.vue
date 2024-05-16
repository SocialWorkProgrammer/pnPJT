<template>
    <div>
       <p>{{comment.content}}</p>
       
    </div>
</template>

<script setup>
defineProps({
    comment: Object,
})
</script>

<style scoped>

</style>