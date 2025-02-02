import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import {createApp} from 'vue'
import {library} from '@fortawesome/fontawesome-svg-core'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import {faCircleXmark} from '@fortawesome/free-regular-svg-icons'
import {faPen} from '@fortawesome/free-solid-svg-icons'
import App from './App.vue'
import helpersPlugin from "@/plugins/helpers";
import applicationPlugin from "@/plugins/application";

library.add(faCircleXmark, faPen)

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(helpersPlugin)
app.use(applicationPlugin)

app.mount('#app')



