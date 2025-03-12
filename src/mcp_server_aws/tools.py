from mcp.types import Tool


def get_s3_tools() -> list[Tool]:
    return [
        Tool(
            name="s3_bucket_create",
            description="Create a new S3 bucket",
            inputSchema={
                "type": "object",
                "properties": {
                    "bucket_name": {
                        "type": "string",
                        "description": "Name of the S3 bucket to create"
                    }
                },
                "required": ["bucket_name"]
            }
        ),
        Tool(
            name="s3_bucket_list",
            description="List all S3 buckets",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="s3_bucket_delete",
            description="Delete an S3 bucket",
            inputSchema={
                "type": "object",
                "properties": {
                    "bucket_name": {
                        "type": "string",
                        "description": "Name of the S3 bucket to delete"
                    }
                },
                "required": ["bucket_name"]
            }
        ),
        Tool(
            name="s3_object_upload",
            description="Upload an object to S3",
            inputSchema={
                "type": "object",
                "properties": {
                    "bucket_name": {
                        "type": "string",
                        "description": "Name of the S3 bucket"
                    },
                    "object_key": {
                        "type": "string",
                        "description": "Key/path of the object in the bucket"
                    },
                    "file_content": {
                        "type": "string",
                        "description": "Base64 encoded file content for upload"
                    }
                },
                "required": ["bucket_name", "object_key", "file_content"]
            }
        ),
        Tool(
            name="s3_object_delete",
            description="Delete an object from S3",
            inputSchema={
                "type": "object",
                "properties": {
                    "bucket_name": {
                        "type": "string",
                        "description": "Name of the S3 bucket"
                    },
                    "object_key": {
                        "type": "string",
                        "description": "Key/path of the object to delete"
                    }
                },
                "required": ["bucket_name", "object_key"]
            }
        ),
        Tool(
            name="s3_object_list",
            description="List objects in an S3 bucket",
            inputSchema={
                "type": "object",
                "properties": {
                    "bucket_name": {
                        "type": "string",
                        "description": "Name of the S3 bucket"
                    }
                },
                "required": ["bucket_name"]
            }
        ),
        Tool(
            name="s3_object_read",
            description="Read an object's content from S3",
            inputSchema={
                "type": "object",
                "properties": {
                    "bucket_name": {
                        "type": "string",
                        "description": "Name of the S3 bucket"
                    },
                    "object_key": {
                        "type": "string",
                        "description": "Key/path of the object to read"
                    }
                },
                "required": ["bucket_name", "object_key"]
            }
        ),
    ]


def get_ec2_tools() -> list[Tool]:
    return [
        Tool(
            name="ec2_instance_list",
            description="List all EC2 instances",
            inputSchema={
                "type": "object",
                "properties": {
                    "filters": {
                        "type": "array",
                        "description": "Optional filters to apply to the instance list",
                        "items": {
                            "type": "object",
                            "properties": {
                                "Name": {"type": "string"},
                                "Values": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            }
                        }
                    }
                }
            }
        ),
        Tool(
            name="ec2_instance_describe",
            description="Describe specific EC2 instances",
            inputSchema={
                "type": "object",
                "properties": {
                    "instance_ids": {
                        "type": "array",
                        "description": "List of EC2 instance IDs to describe",
                        "items": {"type": "string"}
                    }
                },
                "required": ["instance_ids"]
            }
        ),
        Tool(
            name="ec2_instance_start",
            description="Start EC2 instances",
            inputSchema={
                "type": "object",
                "properties": {
                    "instance_ids": {
                        "type": "array",
                        "description": "List of EC2 instance IDs to start",
                        "items": {"type": "string"}
                    }
                },
                "required": ["instance_ids"]
            }
        ),
        Tool(
            name="ec2_instance_stop",
            description="Stop EC2 instances",
            inputSchema={
                "type": "object",
                "properties": {
                    "instance_ids": {
                        "type": "array",
                        "description": "List of EC2 instance IDs to stop",
                        "items": {"type": "string"}
                    },
                    "force": {
                        "type": "boolean",
                        "description": "Force stop the instances",
                        "default": false
                    }
                },
                "required": ["instance_ids"]
            }
        )
    ]


def get_aws_tools() -> list[Tool]:
    return [
        *get_s3_tools(),
        *get_ec2_tools()
    ]
