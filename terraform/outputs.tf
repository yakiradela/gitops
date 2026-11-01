output "cluster_name" {
  value = kind_cluster.default.name
}

output "cluster_endpoint" {
  value = kind_cluster.default.endpoint
}
