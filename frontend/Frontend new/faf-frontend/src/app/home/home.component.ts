import { Component, OnInit, ViewChild, ElementRef,AfterViewChecked } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Chart, registerables } from 'chart.js';
import { Inject, PLATFORM_ID } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import { LeftMenuComponent } from '../left-menu/left-menu.component';
import { trigger, state, style, animate, transition } from '@angular/animations';
import { ApiService } from '../api.service';

// Register all Chart.js components
Chart.register(...registerables);


@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, FormsModule,LeftMenuComponent],  // Add CommonModule to imports
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  animations: [
    trigger('progressAnimation', [
      state('start', style({
        width: '0%'
      })),
      state('end', style({
        width: '{{progress}}%'
      }), { params: { progress: 0 } }),
      transition('start => end', [
        animate('2s ease-out')
      ]),
    ])
  ]
})
export class HomeComponent implements OnInit  {
  selectedTab: number = 1;
  
  years: number[] = [];
  startYear!: number;
  endYear!: number;
  domesticMode: any[] = [];
  commodity: any[] = [];
  domesticDestinations: any[] = [];
  domesticOrigins: any[] = [];

    isRunClicked: boolean = false;

  // Update the onRun method to toggle the button text

  constructor(private apiService: ApiService) {
    const currentYear = new Date().getFullYear();
    const startRange = currentYear -10; // Starting year
    this.years = Array.from({ length: (currentYear + 10) - startRange + 1 }, (_, i) => startRange + i);

  }

  // Function to change the selected tab
  // selectTab(tabNumber: number): void {
  //   this.selectedTab = tabNumber;
  // }

  // ngAfterViewChecked(): void {
  //   if ((this.selectedTab === 1 && !this.chart) || (this.selectedTab === 2 && !this.chart)) {
  //     // Re-create chart only if it's the first tab and chart is not yet created
  //     this.createChart();
  //     this.animateProgressBars();
  //   }

  //   if (this.selectedTab === 3 && !this.pieChart) {
  //     this.createPieChart();
  //   }
  // }

  selectTab(tabNumber: number): void {
    this.selectedTab = tabNumber;
    if ((this.selectedTab === 1) || (this.selectedTab === 2) ) {
      // Delay chart rendering for the current tab
      setTimeout(() => {
        this.createChart();
        this.animateProgressBars();
      }, 2);
    }
 console.log("tabwww",this.selectedTab)
    if (this.selectedTab === 3 ) {
      setTimeout(() => {
        this.createPieChart(); // Create the pie chart when the user comes back to tab 2
      }, 2);
    }
  }

  selectedFlowType: string = '';
  selectedDomesticOrigin: string = '';
  selectedDomesticMode: string = '';
  selectedDomesticDestination: string = '';
  selectedForeignDestination: string = '';
  selectedCommodity: string = '';
  // startYear1: string = '';
  // endYear1: string = '';

  flowTypes = ['Type 1', 'Type 2', 'Type 3'];
  // domesticOrigins = ['Origin 1', 'Origin 2', 'Origin 3'];
  // domesticDestinations = ['Destination 1', 'Destination 2', 'Destination 3'];
  foreignDestinations = ['Foreign 1', 'Foreign 2', 'Foreign 3'];

  chart: any;
  pieChart: any; // Pie chart for imports and exports

  @ViewChild('pieChartCanvas') pieChartCanvas!: ElementRef<HTMLCanvasElement>;

  @ViewChild('chartCanvas') chartCanvas!: ElementRef<HTMLCanvasElement>;

    // Sample import and export data
    importExportData = {
      import: 50,  // Sample data (replace with actual dynamic data)
      export: 30
    };

  ngOnInit(): void {
    // Delay chart initialization to ensure the canvas is rendered
    setTimeout(() => {
      this.createChart();
      this.createPieChart();  
    }, 0);
    this.animateProgressBars();
    this.loadCommodityDetails();
    this.loadTranspotationDetails();
    this.loadDomesticOriginDetails();
    this.loadDomesticDestinationDetails();
  }

  createChart(): void {
    if (this.chart) {
      this.chart.destroy(); // Destroy the previous chart before creating a new ones
    }

    if (this.chartCanvas && this.chartCanvas.nativeElement) {
      const canvas = this.chartCanvas.nativeElement;
      const ctx = canvas.getContext('2d');
      if (ctx) {
        this.chart = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'], // Updated labels for 10 years
            datasets: [{
              label: 'Total Domestic Export (in million tons)', // Dataset label
              data: [15, 18, 20, 25, 22, 30, 35, 40, 42, 45], // Example data
              backgroundColor: 'rgb(78, 148, 183 , 0.6)', // Adjusted color
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
            }]
          },
          options: {
            responsive: true,
            plugins: {
              title: {
                display: true, // Enable the chart title
                text: 'Total Domestic Export Over the Last 10 Years', // Chart title text
                font: {
                  size: 18, // Font size for the title
                  family: 'Arial, sans-serif', // Font family
                  weight: 'bold' // Bold title
                },
                color: '#333', // Title color
                padding: {
                  top: 20,
                  bottom: 10
                }
              }
            },
            scales: {
              y: {
                beginAtZero: true,
                title: {
                  display: true,
                  text: 'Amount (in million tons)', // Y-axis label
                  font: {
                    size: 14
                  }
                }
              },
              x: {
                title: {
                  display: true,
                  text: 'Years', // X-axis label
                  font: {
                    size: 14
                  }
                }
              }
            }
          }
        });
      } else {
        console.error('Failed to get canvas 2D context');
      }
    } else {
      console.error('Canvas element not found');
    }
  }

  progressValues = {
    truck: 0,
    air: 0,
    water: 0,
    rail: 0,
    multipleModes: 0,   // Multiple Modes & Mail progress
    otherUnknown: 0     // Other and Unknown progress
  };

  // Function to get the background style for the progress circle
  getProgressBarStyle(progress: number) {
    const percentage = (progress / 100) * 360;  // Convert percentage to degrees
    return `conic-gradient(#29962d ${percentage}deg, #e0e0e0 ${percentage}deg)`;  // Green progress color
  }
  

  updateChartData(): void {
    if (this.chart) {
      const newData = this.getChartDataForFlowType(this.selectedFlowType);
      this.chart.data.datasets[0].data = newData;
      this.chart.update();
    }
  }

  getChartDataForFlowType(flowType: string): number[] {
    switch (flowType) {
      case 'Type 1':
        return [10, 20, 30, 40, 50];
      case 'Type 2':
        return [15, 25, 35, 45, 55];
      case 'Type 3':
        return [20, 30, 40, 50, 60];
      default:
        return [0, 0, 0, 0, 0];
    }
  }

  onRun(): void {
    this.sendRequest()
    console.log('Run button clicked!');
    // Add your logic here for what should happen when the button is clicked
    console.log('Run button clicked!');
    // this.isRunClicked = true; 

    if (this.isRunClicked) {
      console.log('Download CSV logic goes here');
      // Add logic for downloading CSV or any other action
    } else {
      console.log('Run button clicked!');
      // Add your logic here for what should happen when the button is clicked
    }
    
    // Toggle the button state after each click
    this.isRunClicked = !this.isRunClicked;
  }

  // startYear: number = new Date().getFullYear(); // Default to current year
  // endYear: number = new Date().getFullYear();   // Default to current year

  // Function to handle logic for the selected year range
  updateYearRange() {
    if (this.startYear > this.endYear) {
      alert('Start year must be less than or equal to end year.');
    } else {
      console.log('Selected Year Range:', this.startYear, this.endYear);
    }
  }

  // Reset progress values (if necessary, like when switching tabs)
  // resetProgress() {
  //   this.progressValues = {
  //     truck: 0,
  //     air: 0,
  //     water: 0,
  //     rail: 0,
  //     multipleModes: 0,
  //     otherUnknown: 0
  //   };
  // }

  // // Trigger the animation when coming back to the tab
  // animateProgress() {
  //   // Trigger a small timeout to reset progress to 0 and then animate
  //   setTimeout(() => {
  //     this.progressValues = {
  //       truck: 75,
  //       air: 50,
  //       water: 65,
  //       rail: 85,
  //       multipleModes: 40,
  //       otherUnknown: 10
  //     };
  //   }, 300);
  // }

  isAnimating = true; // Flag to control the animation state

  // constructor() {}


  // Function to animate progress bar from 0 to target value
  animateProgressBars() {
    setTimeout(() => {
      this.setProgress('truck', 65);  // 65% for truck
      this.setProgress('air', 23.45); // 23.45% for air
      this.setProgress('water', 78.92); // 78.92% for water
      this.setProgress('rail', 96.53); // 96.53% for rail
      this.setProgress('multipleModes', 12.65); // 12.65% for multipleModes
      this.setProgress('otherUnknown', 76.51); // 76.51% for otherUnknown
    }, 500); // Delay for initial load
  }

  // Update the progress bar value with ChangeDetection
  setProgress(transport: keyof typeof this.progressValues, value: number): void {
    const step = 1;  // Increment for animation
    let currentValue = 0;
    const interval = setInterval(() => {
      if (currentValue < value) {
        currentValue += step;
        this.progressValues[transport] = currentValue;
      } else {
        clearInterval(interval);
      }
    }, 20);  // Adjust the interval for speed
  }
  

  // Function to get the progress bar style
  // getProgressBarStyle(value: number): number {
  //   return value;
  // }

  hovering: string | null = null;


  // Method to handle mouse enter event
  onHover(transport: string): void {
    this.hovering = transport;
  }

  // Method to handle mouse leave event
  onLeave(): void {
    this.hovering = null;
  }



  createPieChart(): void {
    if (this.pieChart) {
      this.pieChart.destroy();
    }

    if (this.pieChartCanvas && this.pieChartCanvas.nativeElement) {
      const canvas = this.pieChartCanvas.nativeElement;
      const ctx = canvas.getContext('2d');
      if (ctx) {
        this.pieChart = new Chart(ctx, {
          type: 'pie',
          data: {
            labels: ['Import', 'Export'],
            datasets: [{
              data: [this.importExportData.import, this.importExportData.export],
              backgroundColor: [' #507295', '#0b8e74'], // Custom colors for import/export
              borderColor: ['#6ea7c4', '#085e4d'],
              borderWidth: 1
            }]
          },
          options: {
            responsive: true,
            plugins: {
              title: {
                display: true,
                text: 'Import vs Export in Current Year',
                font: {
                  size: 18,
                  family: 'Arial, sans-serif',
                  weight: 'bold'
                },
                color: '#333'
              }
            }
          }
        });
      }
    }
  }

  // sendRequest() {
  //   const payload = {
  //     origin: 'Indiana',
  //     timeframe: [2018, 2025],
  //   };

  //   this.apiService.postDomesticImports(payload).subscribe({
  //     next: (response) => {
  //       console.log('Response:', response);
  //     },
  //     error: (error) => {
  //       console.error('Error:', error);
  //     },
  //   });
  // }

  loadCommodityDetails() {
    this.apiService.loadCommodityDetails().subscribe({
      next: (response) => {
        this.commodity = response;
        console.log('Response:', response);
      },
      error: (error) => {
        console.error('Error:', error);
      },
    });
  }

  loadTranspotationDetails() {
    this.apiService.loadTranspotationDetails().subscribe({
      next: (response) => {
        this.domesticMode = response;
        console.log('Response:', response);
      },
      error: (error) => {
        console.error('Error:', error);
      },
    });
  }


  loadDomesticOriginDetails() {
    this.apiService.loadDomesticOriginDetails().subscribe({
      next: (response) => {
        this.domesticOrigins = response;
        console.log('Response:', response);
      },
      error: (error) => {
        console.error('Error:', error);
      },
    });
  }

  loadDomesticDestinationDetails() {
    this.apiService.loadDomesticDestinationDetails().subscribe({
      next: (response) => {
        this.domesticDestinations = response;
        console.log('Response:', response);
      },
      error: (error) => {
        console.error('Error:', error);
      },
    });
  }


  sendRequest() {
    const payload = {
      origin: this.selectedDomesticOrigin,
      timeframe: [this.startYear, this.endYear],
      commodity: this.selectedCommodity,
      destination: this.selectedDomesticDestination,
      transpotation: this.selectedDomesticMode,
    };

    // Call the API service and handle the CSV file download
    this.apiService.postDomesticImports(payload).subscribe({
      next: (response: Blob) => {
        // Create a download link for the file
        const link = document.createElement('a');
        const url = window.URL.createObjectURL(response);
        link.href = url;
        link.download = 'domestic_imports.csv'; // Set the default download filename
        link.click(); // Trigger the download
        window.URL.revokeObjectURL(url); // Clean up the object URL
      },
      error: (error) => {
        console.error('File download error:', error);
      },
    });
  }
  
}
