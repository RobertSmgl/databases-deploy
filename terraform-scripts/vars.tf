variable ssh-key {
    type    = string
    default = ""
}

variable nodes_map {
    type = map(object({
        name         = string
        resources = object({
            cores         = number
            memory        = number
            gpus          = optional(number)
            core_fraction = optional(number)
        })
        boot_disk = object({
            disk_index = string
        })
        network_interface = object({
            nat          = bool
            subnet_index = string
        })
        metadata = object({
            ssh-keys = optional(string) #user-data = "#cloud-config\nusers:\n  - name: <username>\n    groups: sudo\n    shell: /bin/bash\n    sudo: 'ALL=(ALL) NOPASSWD:ALL'\n    ssh-authorized-keys:\n      - <SSH_key _contents>"
        })
    }))
}

variable boot_disk_map {
    type = map(object({
        name     = string
        size     = number
        zone     = string
        image_id = string
        type     = string
    }))
}

variable subnet_map {
    type = map(object({
        name           = string
        network_index  = string
        v4_cidr_blocks = list(string)
    }))
}

variable network_map {
    type = map(object({
        name = string
    }))
}