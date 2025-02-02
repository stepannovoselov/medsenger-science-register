import HttpClient from "@/utils/http_client";
import AccountActions from "@/api/action_groups/account";
import ProjectActions from "@/api/action_groups/project";
import SubmissionActions from "@/api/action_groups/submission";
import MedsengerActions from "@/api/action_groups/medsenger";

class ApiClient {
    constructor(host, token) {
        let client = new HttpClient(host + '/api')

        this.account = new AccountActions(client, token)
        this.project = new ProjectActions(client, token)
        this.submission = new SubmissionActions(client, token)
        this.medsenger = new MedsengerActions(client, token)

        this.__actionGroups = [this.account, this.project, this.submission, this.medsenger]
    }

    setRole(role) {
        this.__actionGroups.forEach((group) => {
            group.setRole(role)
        })
    }

    setToken(token) {
        this.__actionGroups.forEach((group) => {
            group.setToken(token)
        })
    }
}

export default ApiClient
