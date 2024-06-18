resource "yandex_compute_disk" "postgres" {
    for_each = var.boot_disk_map
    name     = each.value.name
    size     = each.value.size
    zone     = each.value.zone
    image_id = each.value.image_id
    type     = each.value.type 
}