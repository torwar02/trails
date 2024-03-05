import App from './App.vue'
import router from './router'
import { createApp } from 'vue'

import { OhVueIcon, addIcons } from 'oh-vue-icons'
import * as FaIcons from 'oh-vue-icons/icons/fa'
import * as BoIcons from 'oh-vue-icons/icons/bi'
const Fa = Object.values({ ...FaIcons })
const Bi = Object.values({ ...BoIcons })
addIcons(...Fa, ...Bi)

// vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives
})

const app = createApp(App)
app.component('v-icon', OhVueIcon)
app.use(router)
app.use(vuetify)
app.mount('#app')
