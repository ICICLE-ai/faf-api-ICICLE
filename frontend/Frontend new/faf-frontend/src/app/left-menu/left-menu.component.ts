import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-left-menu',
  standalone: true,
  imports: [CommonModule], // Add CommonModule to support *ngFor
  templateUrl: './left-menu.component.html',
  styleUrls: ['./left-menu.component.css']
})
export class LeftMenuComponent {
  menuItems: string[] = ['Reports', 'Overview', 'Version Descriptions', 'About'];

  onMenuItemClick(item: string): void {
    console.log(`Menu item clicked: ${item}`);
  }
}
