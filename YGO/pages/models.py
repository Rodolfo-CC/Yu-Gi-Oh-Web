from django.db import models
from django.utils.translation import gettext_lazy as _

class Card(models.Model):
    """
    Represents a single Yu-Gi-Oh! card.
    """

    class CardType(models.TextChoices):
        MONSTER = "Monster", _("Monster")
        SPELL = "Spell", _("Spell")
        TRAP = "Trap", _("Trap")
    
    class CardAttribute(models.TextChoices):
        LIGHT = "Light", _("Light")
        DARK = "Dark", _("Dark")
        EARTH = "Earth", _("Earth")
        WATER = "Water", _("Water")
        FIRE = "Fire", _("Fire")
        WIND = "Wind", _("Wind")
        DIVINE = "Divine", _("Divine")
    
    class CardRarity(models.TextChoices):
        COMMON = "Common", _("Common")
        RARE = "Rare", _("Rare")
        SUPER_RARE = "Super Rare", _("Super Rare")
        ULTRA_RARE = "Ultra Rare", _("Ultra Rare")
        SECRET_RARE = "Secret Rare", _("Secret Rare")
    
    id = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=100, db_index=True)
    text = models.TextField()
    level = models.PositiveSmallIntegerField(default=0)
    attack = models.PositiveIntegerField(default=0)
    defense = models.PositiveIntegerField(default=0)
    card_type = models.CharField(
        max_length=10,
        choices=CardType.choices,
        db_index=True
    )
    attribute = models.CharField(
        max_length=10,
        choices=CardAttribute.choices,
        db_index=True
    )
    rarity = models.CharField(
        max_length=15,
        choices=CardRarity.choices,
        db_index=True
    )

    def __str__(self):
        """Human-readable string representation of the Card object."""
        return f"{self.name}"
    
    def __repr__(self):
        """Developer-friendly representation of the Card object."""
        return f"<Card id={self.id} name={self.name} type={self.card_type}>"

    class Meta:
        """Meta options for the Card model."""
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["card_type"]),
            models.Index(fields=["attribute"]),
            models.Index(fields=["rarity"]),
        ]
