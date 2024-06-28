from django.db import models

class Alert(models.Model):
    ATTACK_CHOICES = [
        ('DDoS', 'DDoS'),
        ('PortScan', 'Port Scanning'),
        # Add other types of attacks as needed
    ]

    attack_type = models.CharField(max_length=100, choices=ATTACK_CHOICES)
    attacker_ip = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"{self.attack_type} from {self.attacker_ip} at {self.timestamp}"

