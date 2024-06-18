resource "yandex_vpc_network" "postgres" {
    for_each = var.network_map
    name = each.value.name
}

resource "yandex_vpc_gateway" "gateway" {
  name = "egress-gateway"
  shared_egress_gateway {}
}

resource "yandex_vpc_route_table" "postgres" {
  depends_on     = [yandex_vpc_network.postgres]
  network_id = "${yandex_vpc_network.postgres["postgres"].id}"

  static_route {
    destination_prefix = "0.0.0.0/0"
    gateway_id         = "${yandex_vpc_gateway.gateway.id}"
  }
}

resource "yandex_vpc_subnet" "postgres" {
    depends_on     = [yandex_vpc_network.postgres,yandex_vpc_route_table.postgres]
    name           = each.value.name
    for_each       = var.subnet_map
    network_id     = "${yandex_vpc_network.postgres[each.value.network_index].id}"
    v4_cidr_blocks = each.value.v4_cidr_blocks
    route_table_id = "${yandex_vpc_route_table.postgres.id}"
}