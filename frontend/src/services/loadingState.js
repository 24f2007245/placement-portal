import { computed, reactive } from 'vue'

const state = reactive({
  active: 0,
})

const isLoading = computed(() => state.active > 0)

function startLoading() {
  state.active += 1
}

function stopLoading() {
  state.active = Math.max(0, state.active - 1)
}

export { isLoading, startLoading, stopLoading }
