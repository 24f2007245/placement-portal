<script setup>
const props = defineProps({
  label: {
    type: String,
    default: 'Loading',
  },
})
</script>

<template>
  <div class="loading-spinner">
    <span class="spinner" aria-hidden="true"></span>
    <span class="label">{{ props.label }}</span>
  </div>
</template>

<style scoped>
.loading-spinner {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.95);
  color: #2980b9;
  font-size: 0.85rem;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
}

.spinner {
  width: 14px;
  height: 14px;
  border: 2px solid #cfd8dc;
  border-top-color: #2980b9;
  border-radius: 50%;
  display: inline-block;
  animation: spin 0.8s linear infinite;
}

.label {
  line-height: 1;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
