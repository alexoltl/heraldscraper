using HtmlAgilityPack;
using System;
using System.IO;
using System.Windows;

namespace heraldscraper
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private string linkValue;
        private string article;

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Scrape(object sender, RoutedEventArgs e)
        {
            linkValue = link.Text;
            var html = new HtmlWeb().Load(linkValue);
            var paragraphs = html.DocumentNode
                .SelectNodes("//section[contains(@class, 'article__body JeiXlqfBXKkof article__content')]/descendant::p");

            foreach (var p in paragraphs)
            {
                article = article + "\n\n" + p.InnerText;
            }

            using (StreamWriter writer = new StreamWriter("output.txt"))
            {
                writer.WriteLine(article);
            }
        }
    }
}
