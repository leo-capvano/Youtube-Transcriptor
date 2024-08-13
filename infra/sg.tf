resource "aws_security_group" "youtube-loader-sg" {
  name   = "youtube-loader-sg"
  vpc_id = data.aws_vpc.default_vpc.id

  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    description = "allow ssh"
  }

  egress = []
}