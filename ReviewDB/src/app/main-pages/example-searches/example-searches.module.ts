import { NgModule } from '@angular/core';
import { ExampleSearchesComponent } from './example-searches.component';
import { HeaderModule } from '../../main-fragments/header/header.module';
import { FooterModule } from '../../main-fragments/footer/footer.module';

@NgModule({
  declarations: [
    ExampleSearchesComponent,
  ],
  imports: [
    HeaderModule,
    FooterModule,
  ],
  exports: [
    ExampleSearchesComponent,
  ],
})
export class ExampleSearchesModule { }
