<template>
    <div v-if="project">
        <div class="hstack gap-3">
            <div class="me-auto">
                <h4 class="my-3">Список пациентов в проекте "{{ project.name }}"</h4>
            </div>
            <div>
                <button @click="addPatient" class="btn btn-sm btn-primary">Добавить</button>
            </div>
        </div>

        <div class="row my-2" v-if="patients">
            <div class="col">
                <input type="text" placeholder="Поиск..." v-model="searchField" class="form-control"/>
            </div>
        </div>

        <div class="row py-2" v-if="patients">
            <div class="col col-sm-6 col-md-4 col-lg-3 mb-3" v-for="patient in filteredPatients"
                 v-bind:key="patient.id">
                <div class="card">
                    <div class="card-body">
                        <div class="hstack">
                            <div class="me-auto" @click="openPatient(patient)">
                                <h5 class="card-title my-1">{{ patient.name }}</h5>
                            </div>
                            <div @click="editPatient(patient)">
                                <font-awesome-icon :icon="['fas', 'pen']"/>
                            </div>
                        </div>

                        <p class="text-muted my-0">{{ formatDate(patient.birthday) }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>


import {empty, formatDate} from "../utils/helpers";

export default {
    name: 'ProjectPatientsScreen',
    components: {},
    data() {
        return {
            project: undefined,
            patients: [],
            searchField: ''
        }
    },
    computed: {
        filteredPatients: function () {
            return this.patients.filter((patient) => empty(this.searchField) || patient.name.includes(this.searchField))
        }
    },
    methods: {
        formatDate,
        openPatient: function (patient) {
            this.managers.project.openPatientPage(patient)
        },
        loadPatients: async function (project) {
            this.project = project
            this.patients = await this.managers.project.getPatients(project)
            this.sortPatients()
        },
        addPatient: function () {
            this.managers.project.addPatientPage()
        },
        editPatient: function (patient) {
            this.managers.project.editPatientPage(patient)
        },
        sortPatients: function () {
            this.patients.sort((a, b) => a.name.localeCompare(b.name))
        }

    },
    mounted() {
        this.event_bus.on('project-selected', this.loadPatients);
        this.event_bus.on('new-patient', (patient) => {
            this.patients.push(patient)
            this.sortPatients()
        });

        this.event_bus.on('patient-updated', (updated_patient) => {
            this.patients.forEach((patient, i) => {
                if (patient.id === updated_patient.id) {
                    this.patients[i] = updated_patient
                }
            });
            this.sortPatients()
        });
    }
}
</script>

<style scoped>

</style>
