<script setup>
import SideColumn from './SideColumn.vue';


</script>

<template>
    <div v-for="student in source">
        <p>Name: {{ student.name }}</p>
        <p>Resume: {{ student.resume_path }}</p>
        <p>Phone No: {{ student.phone_no }}</p>
        <p>Address: {{ student.address }}</p>
        <p>Social Profiles: {{ student.social_profile }}</p>
    </div>

</template>

<style scoped>
</style>