resource "aws_instance" "ytloader_host" {

  ami                    = "ami-07c8c1b18ca66bb07"
  instance_type          = "t3.micro"
  key_name               = "youtube_loader_kp"
  vpc_security_group_ids = [aws_security_group.youtube-loader-sg.id]

  provisioner "file" {
    source      = "../app.py"
    destination = "/home/ubuntu/app.py"
  }

  provisioner "file" {
    source      = "../requirements.txt"
    destination = "/home/ubuntu/requirements.txt"
  }

  provisioner "file" {
    source      = "../.env_sample"
    destination = "/home/ubuntu/.env"
  }

  provisioner "file" {
    source      = "../src/__init__.py"
    destination = "/home/ubuntu/__init__.py"
  }

  provisioner "file" {
    source      = "../src/llm_chain.py"
    destination = "/home/ubuntu/llm_chain.py"
  }

  provisioner "file" {
    source      = "../src/stuff_chain_svc.py"
    destination = "/home/ubuntu/stuff_chain_svc.py"
  }

  provisioner "file" {
    source      = "../src/youtube_svc.py"
    destination = "/home/ubuntu/youtube_svc.py"
  }

  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ubuntu"
    private_key = file("C:\\Users\\leoca\\Desktop\\youtube_loader_kp.pem")
    timeout     = "4m"
  }
}