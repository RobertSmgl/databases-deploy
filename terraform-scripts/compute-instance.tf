resource "yandex_compute_instance" "postgres" {
    for_each    = var.nodes_map
    depends_on  = [yandex_vpc_subnet.postgres,yandex_compute_disk.postgres]
    name        = each.value.name

    resources {
        cores  = each.value.resources.cores
        memory = each.value.resources.memory
    }

    boot_disk {
        disk_id = yandex_compute_disk.postgres[each.value.boot_disk.disk_index].id
    }

    network_interface {
        nat       = each.value.network_interface.nat
        subnet_id = "${yandex_vpc_subnet.postgres[each.value.network_interface.subnet_index].id}"
    }

    metadata = {
        user-data = each.value.metadata.ssh-keys
    }
}

output private-ips {
    value    = {
        for k,v in yandex_compute_instance.postgres: k => v.network_interface.0.ip_address if v.network_interface.0.nat_ip_address == ""
    }
}

resource "local_file" "private-ips" {
    content  = jsonencode({
        for k,v in yandex_compute_instance.postgres: k => v.network_interface.0.ip_address if v.network_interface.0.nat_ip_address == ""
    })
    filename = "private-ips"
}

output public-ips {
    value    = {
        for k,v in yandex_compute_instance.postgres: k => v.network_interface.0.nat_ip_address if v.network_interface.0.nat_ip_address != ""
    }
}

resource "local_file" "public-ips" {
    content  = jsonencode({
        for k,v in yandex_compute_instance.postgres: k => v.network_interface.0.nat_ip_address if v.network_interface.0.nat_ip_address != ""
    })
    filename = "public-ips"
}

resource "local_file" "all-private-ips" {
    content  = jsonencode({
        for k,v in yandex_compute_instance.postgres: k => v.network_interface.0.ip_address
    })
    filename = "all-private-ips"
}