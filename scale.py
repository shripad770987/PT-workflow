import boto3

def update_service_desired_count(cluster_name, service_name, new_desired_count, region_name):
    # Create a boto3 client for ECS with the specified region
    ecs_client = boto3.client('ecs', region_name=region_name)

    # Update the desired count for the service
    response = ecs_client.update_service(
        cluster=cluster_name,
        service=service_name,
        desiredCount=new_desired_count
    )

    print(f"Updated service '{service_name}' in cluster '{cluster_name}' to desired count: {new_desired_count}")
    print(f"Response: {response}")

if __name__ == "__main__":
    cluster_name = 'default'
    service_name = 'ECS_Runner'
    new_desired_count = 10  # Set the desired count to the new value you want
    region_name = 'us-east-1'  # Set the AWS region you want to use

    update_service_desired_count(cluster_name, service_name, new_desired_count, region_name)
